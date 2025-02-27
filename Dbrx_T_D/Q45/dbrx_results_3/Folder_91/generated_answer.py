from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[2:7].lower()
    chars = defaultdict(int)
    for c in substr:
        if c in english_letters:
            chars[c] += 1
    palindromes = set()
    for c1, count1 in chars.items():
        for c2, count2 in chars.items():
            if c1 != c2:
                palindrome = c1 + c2
                for i in range(count1, 0, -1):
                    for j in range(count2, 0, -1):
                        if i + j - len(palindrome) >= 3:
                            palindromes.add(palindrome + s[7 - i - j:8 - i - j].lower() + palindrome[::-1])
    return palindromes