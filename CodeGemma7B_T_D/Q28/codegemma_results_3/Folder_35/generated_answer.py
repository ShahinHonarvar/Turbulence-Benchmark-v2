def return_nth_smallest_ascii(word):
    func = lambda word: word[50:76]
    lst = sorted(func(word), key=lambda x: ord(x))
    return lst[6]