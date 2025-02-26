def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[1:9]
    for i in range(len(substring)):
        for j in range(i + 3, min(i + 5, len(substring) + 1)):
            potential_palindrome = substring[i:j]
            if potential_palindrome.isalpha():
                if potential_palindrome.lower() == potential_palindrome.lower()[::-1]:
                    result.add(potential_palindrome.lower())
    return result