def palindromes_of_specific_lengths(my_str):
    palindromes = set()
    for i in range(10, 71):
        for j in range(24, 53):
            current_palindrome = my_str[i - j:i].lower()
            if current_palindrome == current_palindrome[::-1]:
                palindromes.add(current_palindrome)
    return palindromes