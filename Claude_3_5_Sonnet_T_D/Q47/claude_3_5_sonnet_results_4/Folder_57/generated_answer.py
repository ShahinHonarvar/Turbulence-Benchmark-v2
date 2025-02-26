def palindromes_of_specific_lengths(string):
    result = set()
    substring = string[16:95]
    lowercase_substring = substring.lower()
    for i in range(len(substring)):
        for length in range(39, 53):
            if i + length > len(substring):
                break
            potential_palindrome = lowercase_substring[i:i + length]
            if potential_palindrome.isalpha() and potential_palindrome == potential_palindrome[::-1]:
                result.add(substring[i:i + length])
    return result