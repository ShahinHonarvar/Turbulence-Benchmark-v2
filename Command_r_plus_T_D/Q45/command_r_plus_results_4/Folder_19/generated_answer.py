def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    for i in range(1, 8):
        substring = s[0:i].lower()
        letters_in_substring = set(substring) & english_letters
        if len(letters_in_substring) == len(substring):
            for j in range(i, len(s)):
                sub_sub_string = s[i:j].lower()
                letters_in_sub_sub_string = set(sub_sub_string) & english_letters
                if len(letters_in_sub_sub_string) == len(sub_sub_string) and is_palindrome(sub_sub_string):
                    palindromes.add(sub_sub_string)
    return palindromes