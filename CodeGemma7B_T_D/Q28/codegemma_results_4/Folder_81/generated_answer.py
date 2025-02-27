def return_nth_smallest_ascii(word):
    count = 0
    for i in range(len(word)):
        if i >= 0 and i <= 13:
            if word[i] <= word[count]:
                count = i
    return word[count]