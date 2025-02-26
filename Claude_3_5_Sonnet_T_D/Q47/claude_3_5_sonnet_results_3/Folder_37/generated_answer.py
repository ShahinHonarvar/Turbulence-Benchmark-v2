def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[:10].lower()
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 6, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            if potential_palindrome.isalpha() and potential_palindrome == potential_palindrome[::-1]:
                result.add(potential_palindrome)
    return result