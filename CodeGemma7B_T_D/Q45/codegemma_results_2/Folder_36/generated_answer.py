def palindromes_between_indices(string):

    def is_palindrome(word):
        return word == word[::-1]
    checked = {}
    ans = set()
    for i in range(5, 9):
        for j in range(i, 9):
            if string[i:j + 1].lower() not in checked:
                if is_palindrome(string[i:j + 1].lower()):
                    ans.add(string[i:j + 1])
                checked[string[i:j + 1].lower()] = True
    return ans