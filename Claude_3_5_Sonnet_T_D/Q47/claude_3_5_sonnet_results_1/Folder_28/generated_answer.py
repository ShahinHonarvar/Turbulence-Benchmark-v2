def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[32:72].lower()
    for i in range(len(substr)):
        for j in range(i + 21, min(i + 33, len(substr) + 1)):
            potential_palindrome = substr[i:j]
            if potential_palindrome.isalpha() and potential_palindrome == potential_palindrome[::-1]:
                result.add(potential_palindrome)
    return result