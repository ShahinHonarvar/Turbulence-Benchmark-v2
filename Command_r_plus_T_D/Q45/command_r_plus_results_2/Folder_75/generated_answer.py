def palindromes_between_indices(s):
    english_letters = [char for char in s[2:5] if char.isalpha()]
    english_letters = [char.lower() for char in english_letters]
    unique_letters = list(set(english_letters))
    palindromes = set()
    for i in range(len(unique_letters)):
        for j in range(i + 1, len(unique_letters)):
            first_half = unique_letters[i:j]
            second_half = first_half[::-1]
            palindrome = ''.join(first_half + second_half)
            palindromes.add(palindrome)
    return palindromes