def palindromes_of_specific_lengths(s):
    sub_s = s[43:96]
    palindromes = set()
    for length in range(18, 48):
        for start in range(0, len(sub_s) - length + 1):
            substring = sub_s[start:start + length]
            is_palindrome = substring.lower() == substring.lower()[::-1]
            only_letters = all((c.isalpha() for c in substring))
            if is_palindrome and only_letters:
                palindromes.add(substring)
    return palindromes