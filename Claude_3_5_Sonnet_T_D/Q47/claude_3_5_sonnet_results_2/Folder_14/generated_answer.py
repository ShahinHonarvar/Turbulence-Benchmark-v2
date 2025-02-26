def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[10:75]
    for i in range(len(substring)):
        for length in range(6, 9):
            if i + length <= len(substring):
                potential_palindrome = substring[i:i + length]
                if potential_palindrome.isalpha():
                    if potential_palindrome.lower() == potential_palindrome.lower()[::-1]:
                        result.add(potential_palindrome)
    return result