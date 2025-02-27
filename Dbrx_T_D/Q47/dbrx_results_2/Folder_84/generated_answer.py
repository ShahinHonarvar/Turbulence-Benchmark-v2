def palindromes_of_specific_lengths(s):
    english_letters = set((chr(i) for i in range(ord('a'), ord('z') + 1) | set((chr(i) for i in range(ord('A'), ord('Z') + 1)))))
    palindrome_set = set()
    for length in range(13, 41):
        for start in range(23, 78 - length + 1):
            substring = s[start:start + length]
            if len(substring) == len(set(substring) & english_letters) == length:
                substr_lower = substring.lower()
                if substr_lower == substr_lower[::-1]:
                    palindrome_set.add(substr_lower)
    return palindrome_set