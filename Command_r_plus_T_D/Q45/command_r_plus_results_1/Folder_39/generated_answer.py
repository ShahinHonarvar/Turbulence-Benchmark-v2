def palindromes_between_indices(s):
    english_letters = [char for char in s[2:6] if char.isalpha()]
    english_letters = [char.lower() for char in english_letters]
    unique_letters = list(set(english_letters))
    palindromes = set()
    for i in range(len(unique_letters)):
        for j in range(i + 1, len(unique_letters)):
            letter_pair = [unique_letters[i], unique_letters[j]]
            if english_letters.count(letter_pair[0]) >= 2 and english_letters.count(letter_pair[1]) >= 1:
                palindrome = letter_pair[0] * 2 + letter_pair[1]
                palindromes.add(palindrome)
            if english_letters.count(letter_pair[0]) >= 1 and english_letters.count(letter_pair[1]) >= 2:
                palindrome = letter_pair[0] + letter_pair[1] * 2
                palindromes.add(palindrome)
    return palindromes