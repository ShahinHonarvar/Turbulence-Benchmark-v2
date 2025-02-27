from collections import deque

def palindromes_of_specific_lengths(string):
    res = set()
    for i in range(119, 257):
        for size in range(104, 124):
            win = deque(maxlen=size)
            rol = i - size + 1
            for j in range(i, rol - 1, -1):
                win.appendleft(string[j].lower())
                if len(win) == size and win[0] == win[-1]:
                    res.add(''.join(win))
    return res