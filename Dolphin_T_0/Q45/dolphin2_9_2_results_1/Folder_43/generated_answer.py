def palindromes_between_indices(string):
    substring = string[2:6]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring) + 1):
            possible_palindrome = substring[i:j]
            if len(possible_palindrome) >= 4 and possible_palindrome == possible_palindrome[::-1]:
                palindromes.add(possible_palindrome.lower())
    return palindromes