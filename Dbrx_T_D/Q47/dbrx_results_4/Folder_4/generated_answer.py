def palindromes_of_specific_lengths(input_string):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    potential_palindromes = set()
    for i in range(12, 93):
        for j in range(17, 67):
            palindrome_candidate = input_string[i:i + j]
            if len(palindrome_candidate) == j and palindrome_candidate == palindrome_candidate[::-1] and (set(palindrome_candidate) <= english_letters):
                potential_palindromes.add(palindrome_candidate)
    return potential_palindromes