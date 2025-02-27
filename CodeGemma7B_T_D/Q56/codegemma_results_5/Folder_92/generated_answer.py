def all_substring_of_size_n(text):

    def backtrack(current, picked):
        if len(picked) == n:
            result.append(''.join(picked))
            return
        for char in current:
            if char not in picked:
                picked.append(char)
                backtrack(current[1:], picked)
                picked.pop()
    n = 9
    result = []
    backtrack(text, [])
    return result