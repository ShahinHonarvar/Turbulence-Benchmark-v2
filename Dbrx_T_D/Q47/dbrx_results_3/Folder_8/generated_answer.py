def palindromes_of_specific_lengths(input_string):
    valid_palindromes = set()
    for i in range(17, 73):
        substring = input_string[i:i + 51].lower()
        for j in range(50, 52):
            palindrome = substring[j - 50:j]
            if palindrome and palindrome == palindrome[::-1] and palindrome.isalpha():
                valid_palindromes.add(palindrome)
    return valid_palindromes