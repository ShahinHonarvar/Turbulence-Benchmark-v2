def palindromes_between_indices(input_str):
    letters = set((char.lower() for char in input_str[1:4] if char.isalpha()))
    palindromes = set()
    for first_letter in letters:
        for second_letter in letters:
            for third_letter in letters:
                for fourth_letter in letters:
                    palindrome = first_letter + second_letter + third_letter + fourth_letter
                    if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
    return palindromes