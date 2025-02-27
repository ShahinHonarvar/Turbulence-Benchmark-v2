def palindrome_of_length_at_least_n(word):
    char_list = list(word)
    palindrome_set = set()
    word = word.lower()
    n = 33
    middle_index = int(len(word) / 2) - 1
    palindrome_set = set()
    for i in range(middle_index + 1):
        for j in range(i + 1, len(word) - middle_index - 1):
            if word[i] == word[j]:
                palindrome = char_list[i]
                for k in range(i + 1, j):
                    palindrome += word[k]
                palindrome += char_list[j]
                if len(palindrome) >= n:
                    palindrome_set.add(palindrome)
    return palindrome_set