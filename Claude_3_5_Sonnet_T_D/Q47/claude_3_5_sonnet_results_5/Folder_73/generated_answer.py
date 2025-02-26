def palindromes_of_specific_lengths(s):
    result = set()
    substr = s[21:63]
    for i in range(len(substr)):
        for j in range(i + 22, min(i + 34, len(substr) + 1)):
            potential_palindrome = substr[i:j]
            if potential_palindrome.isalpha():
                if potential_palindrome.lower() == potential_palindrome.lower()[::-1]:
                    result.add(potential_palindrome)
    return result