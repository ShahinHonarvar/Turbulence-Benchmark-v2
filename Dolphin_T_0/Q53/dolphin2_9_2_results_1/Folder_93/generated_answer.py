def get_palindromes(word: str, length: int) -> set:
    palindromes = set()
    for i in range(len(word) - length + 1):
        sub_word = word[i:i + length]
        if sub_word == sub_word[::-1]:
            palindromes.add(sub_word)
    return palindromes

def palindrome_of_length_at_least_n(word: str) -> set:
    word = word.lower()
    palindromes = get_palindromes(word, 90)
    if not palindromes:
        return get_palindromes(word, 2)
    return palindromes