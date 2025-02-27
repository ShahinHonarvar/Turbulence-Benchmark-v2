def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        substr_letters_only = ''.join((c for c in substr if c.isalpha()))
        return substr_letters_only.lower() == substr_letters_only[::-1].lower()
    result = set()
    filtered_string = s[16:95]
    for length in range(39, 53):
        for i in range(len(filtered_string) - length + 1):
            substr = filtered_string[i:i + length]
            if is_palindrome(substr):
                result.add(substr)
    return result