def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[28:95]
    for length in range(38, 50):
        for i in range(len(substring) - length + 1):
            potential_palindrome = substring[i:i + length]
            if potential_palindrome == potential_palindrome[::-1] and potential_palindrome.isalpha():
                result.add(potential_palindrome.lower())
    return result