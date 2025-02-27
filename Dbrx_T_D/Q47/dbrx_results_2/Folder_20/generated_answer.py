def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for length in range(36, 43):
        for start in range(20, len(input_string) - length + 1):
            palindrome_candidate = input_string[start:start + length]
            if set(palindrome_candidate) <= english_letters and palindrome_candidate == palindrome_candidate[::-1]:
                palindromes.add(palindrome_candidate.lower())
    return palindromes