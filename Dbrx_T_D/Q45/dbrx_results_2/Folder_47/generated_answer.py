from collections import defaultdict

def palindromes_between_indices(s):
    s = s[3:8].lower()
    chars = defaultdict(int)
    for char in s:
        chars[char] += 1
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            chars[s[j]] -= 1
            if all((count % 2 == 0 for count in chars.values())):
                palindrome = ''.join((char for count in chars.values() for char in [s[j]] * count))
                if len(palindrome) >= 5:
                    palindromes.add(palindrome)
            chars[s[j]] += 1
    return palindromes