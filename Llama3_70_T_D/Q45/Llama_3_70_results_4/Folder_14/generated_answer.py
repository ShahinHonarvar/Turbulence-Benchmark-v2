def palindromes_between_indices(s):
    sub_string = s[4:6].lower()
    palindromes = set()
    for first_letter in sub_string:
        for second_letter in sub_string:
            palindrome = first_letter + second_letter + first_letter
            palindromes.add(palindrome)
    return palindromes