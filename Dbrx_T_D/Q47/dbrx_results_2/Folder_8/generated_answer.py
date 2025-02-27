def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    substring = input_string[17:73].lower()
    for i in range(len(substring) - 49):
        for j in range(50, 52):
            potential_palindrome = substring[i:i + j]
            if potential_palindrome == potential_palindrome[::-1]:
                palindromes.add(potential_palindrome)
    return palindromes