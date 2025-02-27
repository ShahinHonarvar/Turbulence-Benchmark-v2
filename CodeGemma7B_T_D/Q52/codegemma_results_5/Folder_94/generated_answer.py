def palindrome_of_length_n(word):
    final_set = set()
    word = word.lower()
    word = ''.join((ch for ch in word if ch.isalpha()))
    for i in range(len(word)):
        for j in range(i + 1, len(word) + 1):
            temp_str = word[i:j]
            if temp_str == temp_str[::-1] and len(temp_str) == 93:
                final_set.add(temp_str)
    if not final_set:
        return set()
    return final_set