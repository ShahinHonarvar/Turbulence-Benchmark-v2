def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[103:277]
    substring = ''.join(filter(str.isalpha, substring)).lower()
    for start in range(len(substring)):
        for length in range(100, 170):
            if start + length > len(substring):
                break
            potential_palindrome = substring[start:start + length]
            if potential_palindrome == potential_palindrome[::-1]:
                result.add(potential_palindrome)
    return result