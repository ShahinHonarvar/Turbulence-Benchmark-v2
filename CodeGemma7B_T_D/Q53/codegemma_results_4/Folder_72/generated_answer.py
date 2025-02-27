def palindrome_of_length_at_least_n(str):
    length = len(str)
    ans = set()
    for i in range(length - 87):
        for j in range(i + 88, length):
            word = str[i:j + 1]
            if word == word[::-1]:
                ans.add(word)
    return ans