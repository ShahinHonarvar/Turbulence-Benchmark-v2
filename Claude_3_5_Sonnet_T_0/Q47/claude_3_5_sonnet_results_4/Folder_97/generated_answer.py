def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[28:95]
    for i in range(len(substring)):
        for j in range(i + 38, min(i + 50, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 38 <= len(potential_palindrome) <= 49:
                result.add(potential_palindrome)
    return result