def palindromes_of_specific_lengths(s):
    set_palindromes = set()
    for length in range(104, 124):
        for substring in range(119, 257):
            if s[substring:substring + length].lower() == s[substring:substring + length].lower()[::-1]:
                set_palindromes.add(s[substring:substring + length])
    return set_palindromes