def palindromes_of_specific_lengths(text):
    palindromes = set()
    substring = text[11:97]
    for i in range(len(substring) - 44):
        for j in range(i + 45, min(i + 53, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            if potential_palindrome.isalpha() and potential_palindrome.lower() == potential_palindrome.lower()[::-1]:
                palindromes.add(potential_palindrome)
    return palindromes