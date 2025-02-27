def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(13, 41):
        for start in range(23, 78 - length + 1):
            if s[start:start + length].lower() == s[start:start + length][::-1].lower():
                is_palindrome = all((c.isalpha() for c in s[start:start + length]))
                if is_palindrome:
                    palindromes.add(s[start:start + length])
    return palindromes