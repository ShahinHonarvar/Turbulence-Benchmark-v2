def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[18:89]
    for i in range(len(substring)):
        for j in range(i + 12, min(i + 15, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            if potential_palindrome.isalpha():
                if potential_palindrome.lower() == potential_palindrome.lower()[::-1]:
                    result.add(potential_palindrome)
    return result