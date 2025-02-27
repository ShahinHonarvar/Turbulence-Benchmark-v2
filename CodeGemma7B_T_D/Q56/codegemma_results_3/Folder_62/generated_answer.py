def all_substring_of_size_n(text):

    def subseq(index):
        if index == len(text):
            return ['']
        result = []
        prev = None
        for c in subseq(index + 1):
            if c == '':
                result.append(text[index])
            elif c[0] != text[index] or c[0] == prev:
                result.append(text[index] + c)
            prev = c[0]
        return result
    return [s for s in subseq(0) if len(s) == 32]