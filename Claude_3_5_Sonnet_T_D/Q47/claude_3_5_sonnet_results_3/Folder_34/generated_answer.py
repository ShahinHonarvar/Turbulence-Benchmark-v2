def palindromes_of_specific_lengths(s):
    substring = s[200:301]
    result = set()
    for i in range(len(substring)):
        for j in range(i + 10, min(i + 51, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 10 <= len(potential_palindrome) <= 50:
                result.add(potential_palindrome)
    return result