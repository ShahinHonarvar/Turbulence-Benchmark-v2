def palindromes_of_specific_lengths(input_string):
    palindrome_set = set()
    for i in range(18, 89):
        for j in range(12, 15):
            candidate_palindrome = input_string[i:i + j].lower()
            if candidate_palindrome == candidate_palindrome[::-1] and input_string[i:i + j].isalpha():
                palindrome_set.add(candidate_palindrome)
    return palindrome_set