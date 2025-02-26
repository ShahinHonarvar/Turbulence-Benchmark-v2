def palindromes_of_specific_lengths(s):

    def is_palindrome(substr):
        return substr == substr[::-1]

    def is_letters_only(substr):
        return substr.isalpha()
    substring = s[100:301]
    results = set()
    for length in range(50, 101):
        for start in range(len(substring) - length + 1):
            potential_palindrome = substring[start:start + length]
            if is_palindrome(potential_palindrome.lower()) and is_letters_only(potential_palindrome):
                results.add(potential_palindrome)
    return results