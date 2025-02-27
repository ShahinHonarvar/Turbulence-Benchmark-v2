def palindromes_of_specific_lengths(s):
    valid_palindromes = set()
    for length in range(104, 121):
        for index in range(155, 284 - length + 1):
            if s[index:index + length].lower() == s[index:index + length][::-1].lower():
                valid_palindromes.add(s[index:index + length])
    return valid_palindromes