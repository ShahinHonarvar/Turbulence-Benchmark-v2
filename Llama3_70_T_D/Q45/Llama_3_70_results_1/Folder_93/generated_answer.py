def palindromes_between_indices(input_string):
    substring = input_string[2:8].lower()
    letters = [char for char in substring if char.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            first_half = letters[i:i + (length + 1) // 2]
            second_half = first_half[:length // 2][::-1]
            palindrome = ''.join(first_half + second_half)
            palindromes.add(palindrome)
    return palindromes