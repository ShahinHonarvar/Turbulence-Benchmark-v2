def palindromes_between_indices(s):

    def is_palindrome(check):
        return check == check[::-1]
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 7:
        return set()
    else:
        letters = letters[1:8]
        and_letters = set()
        for i in letters:
            and_letters.add(i)
        all_palindromes = set()
        for word in and_letters:
            if is_palindrome(word):
                all_palindromes.add(word)
        return all_palindromes