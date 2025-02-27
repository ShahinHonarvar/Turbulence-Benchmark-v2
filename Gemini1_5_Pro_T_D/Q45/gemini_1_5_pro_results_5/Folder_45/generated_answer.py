from collections import Counter

def palindromes_between_indices(s):
    s = s.lower()
    letters = ''.join((c for c in s[5:10] if c.isalpha()))
    letters_count = Counter(letters)
    palindromes = set()
    for length in range(4, len(letters) + 1):
        half_length = length // 2
        for chars in letters_count.combinations(half_length):
            if length % 2 == 0:
                palindrome = ''.join(chars) + ''.join(reversed(chars))
                if len(palindrome) >= 4:
                    palindromes.add(palindrome)
            else:
                for middle_char in letters_count:
                    if letters_count[middle_char] >= 1:
                        palindrome = ''.join(chars) + middle_char + ''.join(reversed(chars))
                        if len(palindrome) >= 4:
                            palindromes.add(palindrome)
    return palindromes