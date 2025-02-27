def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for i in range(26, 88):
        for j in range(i, 88):
            current_palindrome = string[i:j + 1]
            if current_palindrome == current_palindrome[::-1] and len(current_palindrome) in range(52, 57):
                palindromes.add(current_palindrome)
    return palindromes