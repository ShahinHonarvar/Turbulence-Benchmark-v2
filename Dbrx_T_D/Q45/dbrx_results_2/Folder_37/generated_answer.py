from functools import reduce

def palindromes_between_indices(s: str) -> set:

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    def group_by_letter(c: str) -> set:
        letter_regex = '[a-zA-Z]'
        return {word for word in words if word.count(c) > 0}

    def filter_palindromes(words: set) -> set:
        return {word for word in words if is_palindrome(word)}

    def filter_length(words: set) -> set:
        return {word for word in words if len(word) >= 5}
    words = {s[index] for index in range(5)}
    words = reduce(group_by_letter, words, set())
    words = filter_palindromes(words)
    words = filter_length(words)
    return words