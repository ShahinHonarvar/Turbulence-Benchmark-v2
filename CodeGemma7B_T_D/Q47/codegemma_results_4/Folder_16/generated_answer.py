def palindromes_of_specific_lengths(string):
    result = set()
    for start in range(15, 87):
        for end in range(51, 61):
            palindrome = string[start:start + end]
            if palindrome == palindrome[::-1]:
                result.add(palindrome.lower())
    return result