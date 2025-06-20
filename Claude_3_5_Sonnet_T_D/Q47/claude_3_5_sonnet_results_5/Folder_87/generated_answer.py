def palindromes_of_specific_lengths(s):
    substring = s[11:94]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 34, min(i + 55, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            if potential_palindrome.isalpha():
                if potential_palindrome.lower() == potential_palindrome.lower()[::-1]:
                    result.add(potential_palindrome)
    return result