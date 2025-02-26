def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[124:284]
    for i in range(len(substring)):
        for j in range(i + 115, min(i + 135, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j])).lower()
            if potential_palindrome == potential_palindrome[::-1] and 115 <= len(potential_palindrome) <= 134:
                result.add(potential_palindrome)
    return result