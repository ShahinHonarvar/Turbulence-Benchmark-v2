def palindromes_between_indices(s):
    s = s.lower()
    english_letters = [char for char in s[4:9] if char.isalpha()]
    unique_letters = set(english_letters)
    palindromes = set()
    for letter in unique_letters:
        if english_letters.count(letter) % 2 == 0:
            palindromes.add(letter * (english_letters.count(letter) // 2))
    palindromes = ''.join(palindromes)
    return {palindrome for palindrome in palindromes if len(palindrome) >= 5}