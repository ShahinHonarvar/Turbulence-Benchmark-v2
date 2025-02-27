def filter_chars(instr):
    for i in range(320, 337):
        instr = instr.replace(instr[i], '')
    return instr