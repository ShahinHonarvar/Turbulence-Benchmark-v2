def palindrome_of_length_n(a):
    no = set()

    def check_palindrome(word):
        for i in range(len(word) // 2):
            if word[i] != word[len(word) - i - 1]:
                return False
        return True
    for i in range(len(a)):
        for j in range(i + 1, i + 84):
            if check_palindrome(a[i:j + 1]):
                no.add(a[i:j + 1])
    if not no:
        no.add('no palindrome found')
    return no